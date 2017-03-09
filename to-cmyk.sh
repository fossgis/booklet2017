#! /usr/bin/env bash

gs -o $2 -sDEVICE=pdfwrite -sProcessColorModel=DeviceCMYK -sColorConversionStrategy=CMYK -sColorConversionStrategyForImages=CMYK -q $1
