// Worker: serves /audio/* from R2, everything else from static assets
export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    // Serve audio files from R2
    if (url.pathname.startsWith('/audio/')) {
      const key = 'family-audio/' + url.pathname.slice(7); // strip /audio/
      const object = await env.AUDIO_BUCKET.get(key);

      if (!object) {
        return new Response('Not found', { status: 404 });
      }

      return new Response(object.body, {
        headers: {
          'Content-Type': 'audio/mpeg',
          'Cache-Control': 'public, max-age=31536000, immutable',
          'Accept-Ranges': 'bytes',
        },
      });
    }

    // Everything else: let assets binding handle it
    return env.ASSETS.fetch(request);
  },
};
