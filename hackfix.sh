#!/usr/bin/env bash


# HACK TO FIX PROBLEM WITH
# Conversion error: Jekyll::Converters::Scss encountered an error while converting 'assets/css/style.scss':
# Invalid US-ASCII character "\xE2" on line 5

find ./vendor/bundle -name typography.scss -exec ./prepend_line.sh '@charset "utf-8";' {} \; 

echo "Done."
