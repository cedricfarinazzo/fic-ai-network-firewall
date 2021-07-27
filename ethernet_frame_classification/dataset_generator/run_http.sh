#!/bin/bash

rawurlencode() {
    echo "$(perl -MURI::Escape -e 'print uri_escape($ARGV[0]);' "$1")"
}


while IFS= read -r line
do
  curl "$2/$(rawurlencode "$line")" > /dev/null
done < "$1"
