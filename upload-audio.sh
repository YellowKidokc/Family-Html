#!/usr/bin/env bash
# Upload all MP3 files from Family/ to R2 bucket under family-audio/ prefix
# Usage: bash upload-audio.sh

BUCKET="theophysics-storage"
PREFIX="family-audio"

echo "Uploading audio to R2 bucket: $BUCKET/$PREFIX/"
echo "---"

for f in Family/*.mp3; do
  filename=$(basename "$f")
  # Convert to URL-safe name: lowercase, spaces to hyphens
  safe=$(echo "$filename" | tr '[:upper:]' '[:lower:]' | tr ' ' '-')
  echo "  $filename -> $PREFIX/$safe"
  npx wrangler r2 object put "$BUCKET/$PREFIX/$safe" --file="$f" --content-type="audio/mpeg" --remote
done

echo "---"
echo "Done. Files available at: /audio/<filename>"
echo "Run 'npx wrangler deploy' to deploy the worker that serves them."
