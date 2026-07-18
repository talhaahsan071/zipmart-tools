"""
ZipMart — Watermark + WebP Converter
======================================
- Adds ZipMart logo (bottom-left, 20% opacity)
- Converts all images to WebP format (better SEO, smaller size)
- Sharpens image slightly for better quality
- Saves to watermarked_images\ folder

USAGE:
    py watermark_webp.py
"""

from PIL import Image, ImageEnhance, ImageFilter
import os
import re

INPUT_FOLDER    = "product_images"
OUTPUT_FOLDER   = "watermarked_images"
LOGO_FILE       = "zipmart_logo.png"
LOGO_OPACITY    = 0.20
LOGO_SIZE_RATIO = 0.20
PADDING         = 15
WEBP_QUALITY    = 92   # 92% quality — excellent balance of size vs quality


def process_image(image_path, output_path, logo):
    try:
        img = Image.open(image_path).convert("RGBA")
        img_w, img_h = img.size

        # ── Sharpen slightly for better quality ──────────────────
        img_rgb = img.convert("RGB")
        img_rgb = img_rgb.filter(ImageFilter.UnsharpMask(radius=1, percent=120, threshold=3))
        img = img_rgb.convert("RGBA")

        # ── Resize logo to 20% of image width ───────────────────
        logo_w = int(img_w * LOGO_SIZE_RATIO)
        logo_h = int(logo_w * (logo.size[1] / logo.size[0]))
        logo_resized = logo.resize((logo_w, logo_h), Image.LANCZOS)

        # ── Apply opacity ────────────────────────────────────────
        r, g, b, a = logo_resized.split()
        a = ImageEnhance.Brightness(a).enhance(LOGO_OPACITY)
        logo_resized.putalpha(a)

        # ── Paste logo bottom-left ───────────────────────────────
        watermarked = img.copy()
        x = PADDING
        y = img_h - logo_h - PADDING
        watermarked.paste(logo_resized, (x, y), logo_resized)

        # ── Save as WebP ─────────────────────────────────────────
        final = watermarked.convert("RGB")
        final.save(output_path, "WEBP", quality=WEBP_QUALITY, method=6)

        return True

    except Exception as e:
        print(f"  !! Error: {e}")
        return False


def main():
    print("=" * 55)
    print("  ZipMart — Watermark + WebP Converter")
    print("=" * 55)

    if not os.path.exists(LOGO_FILE):
        print(f"\n[!] Logo not found: {LOGO_FILE}")
        return

    if not os.path.exists(INPUT_FOLDER):
        print(f"\n[!] Folder not found: {INPUT_FOLDER}")
        return

    logo = Image.open(LOGO_FILE).convert("RGBA")
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    valid_ext = {".jpg", ".jpeg", ".png", ".webp"}
    all_images = [
        f for f in os.listdir(INPUT_FOLDER)
        if os.path.splitext(f)[1].lower() in valid_ext
    ]

    print(f"\n✅ Images found  : {len(all_images)}")
    print(f"✅ Output folder : {OUTPUT_FOLDER}\\")
    print(f"✅ Format        : WebP (quality {WEBP_QUALITY}%)")
    print(f"✅ Logo opacity  : {int(LOGO_OPACITY*100)}%")
    print(f"\nProcessing...\n")

    success = 0
    failed  = 0
    skipped = 0

    for i, filename in enumerate(all_images, 1):
        # Output filename always .webp
        base = os.path.splitext(filename)[0]
        output_filename = base + ".webp"
        input_path  = os.path.join(INPUT_FOLDER, filename)
        output_path = os.path.join(OUTPUT_FOLDER, output_filename)

        # Skip if already done
        if os.path.exists(output_path):
            skipped += 1
            print(f"[{i}/{len(all_images)}] ⏭ {output_filename} — already exists")
            continue

        result = process_image(input_path, output_path, logo)

        if result:
            success += 1
            print(f"[{i}/{len(all_images)}] ✅ {output_filename}")
        else:
            failed += 1
            print(f"[{i}/{len(all_images)}] ✗  {filename} — failed")

        if i % 100 == 0:
            print(f"\n  💾 Progress: {i}/{len(all_images)} done\n")

    print(f"\n{'='*55}")
    print(f"✅ DONE!")
    print(f"   Converted : {success} images → WebP")
    print(f"   Skipped   : {skipped} already done")
    print(f"   Failed    : {failed}")
    print(f"   Saved in  : {OUTPUT_FOLDER}\\")
    print(f"{'='*55}")


if __name__ == "__main__":
    main()
