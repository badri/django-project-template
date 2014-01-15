#!/bin/sh
python manage.py sqlclear $1 | sed 's/";/" CASCADE;/'
