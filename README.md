# ZipMart Automation Pipeline

An end-to-end automation system for running an electronics/gadgets e-commerce store on WooCommerce — built to eliminate manual product listing work by handling sourcing, image processing, import, and SEO in one pipeline.

**Live store:** [zipmart.pk](https://zipmart.pk)

## Overview

Sourcing and listing products manually on WooCommerce is slow and error-prone at scale — images need cleanup, titles and meta descriptions need to be SEO-ready, and category structures get messy fast. This project automates that entire flow, from raw supplier data to a fully published, SEO-optimized product listing.

## Pipeline Stages

### 1. Product Scraping
Pulls product data (titles, prices, specs, images) from the supplier source ([computerzone.pk](https://computerzone.pk)) and structures it for import.

### 2. Image Processing
- Watermarks product images with store branding
- Converts images to WebP for faster page load and better Core Web Vitals

### 3. WooCommerce Import
Pushes structured product data directly into WooCommerce via the REST API — handling variations, pricing, and stock in bulk instead of manual entry.

### 4. SEO Field Population
Automatically populates Rank Math SEO fields (focus keyword, meta title, meta description) for every imported product via the WordPress REST API, so nothing goes live without basic on-page SEO in place.

## Tech Stack
- WooCommerce (WordPress)
- WordPress REST API
- Rank Math SEO (API integration)
- Python (scraping, image processing, API calls)

## Status
Core pipeline is functional end-to-end. Current focus areas:
- Cleaning up remaining auto-generated product titles/meta descriptions
- Fixing duplicate and scattered category structure
- Mobile responsiveness fixes on the homepage

## Author
**Talha Ahsan** — SEO Specialist & Digital Marketer
[LinkedIn](https://www.linkedin.com/in/talhaahsanofficial) · [Portfolio](https://zipmart.pk)
