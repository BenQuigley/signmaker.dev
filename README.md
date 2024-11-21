# signmaker.dev

Source code for Ben Quigley's homepage, online at [signmaker.dev](https://signmaker.dev).

## Setup

``` shell
git clone https://github.com/BenQuigley/signmaker.dev
cd signmaker.dev
virtualenv env
env/bin/pip install -r requirements.lock
git clone https://github.com/getpelican/pelican-plugins
git clone https://gitlab.com/bquigley/Flex/ themes/Flex
make devserver
```
