// Worker: serves /audio/* from R2, everything else from static assets
export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    // Serve audio files from R2
    if (url.pathname.startsWith('/audio/')) {
      const key = 'family-audio/' + url.pathname.slice(7); // strip /audio/

      try {
        const object = await env.AUDIO_BUCKET.get(key);

        if (!object) {
          return new Response(`Not found: ${key}`, { status: 404 });
        }

        const headers = new Headers();
        headers.set('Content-Type', object.httpMetadata?.contentType || 'audio/mpeg');
        headers.set('Cache-Control', 'public, max-age=31536000, immutable');
        headers.set('Accept-Ranges', 'bytes');
        headers.set('Content-Length', object.size);
        headers.set('ETag', object.httpEtag);

        return new Response(object.body, { headers });
      } catch (e) {
        return new Response(`Error: ${e.message}`, { status: 500 });
      }
    }

    // Everything else: let assets binding handle it
    return env.ASSETS.fetch(request);
  },
};
