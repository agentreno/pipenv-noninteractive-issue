# pipenv-noninteractive-issue

Demonstrates issue using pipenv to manage dependencies in a non-interactive
environment like the Vagrant shell provisioner.

Just run `vagrant up` and watch the build output as it runs the commands in the
Vagrantfile, it fails at the pipenv shell step.
