#!/usr/bin/env bash


export LC_ALL="C.UTF-8"
export LANG="en_US.UTF-8"
export LANGUAGE="en_US.UTF-8"

echo "Installing software needed to run Jekyll locally... "
[[ -s "$HOME/.rvm/scripts/rvm" ]] && source "$HOME/.rvm/scripts/rvm" 

rvm use 2.4.2

bundle exec jekyll serve
