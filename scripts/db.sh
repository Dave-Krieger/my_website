#!/bin/bash
read -n1 -p "1 to push, 2 to pull" doit
case $doit in

  1)
  heroku pg:reset --confirm krieger-website
  heroku pg:push my_database DATABASE_URL --app krieger-website ;;

  2)

  dropdb my_database
  createdb my_database
  heroku pg:pull DATABASE_URL my_database --app krieger-website ;;

  *) echo "INVALID" ;;

esac
