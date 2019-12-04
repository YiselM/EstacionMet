#!/bin/bash
date=$(curl -s --head http://google.com | grep ^Date: | sed 's/Date: //g')
out=$(sudo date -s "$date")