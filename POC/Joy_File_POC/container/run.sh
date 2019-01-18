#!/bin/bash
PATH="user/server/app"
killall -9 node
cd $PATH
npm run dev
