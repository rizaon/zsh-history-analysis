#!/bin/bash

mkdir -p raw

set -x
while read SERVER; do
  rsync $SERVER:~/.zsh_history raw/$SERVER-zsh_history
done<servers
