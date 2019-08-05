#!/bin/bash

sudo date -s "$(wget --no-cache -S -O /dev/null google.com 2>&1 | \sed -n -e '/  *Date: */ {' -e s///p -e q -e '}')"

