AUTHOR = "Ben Quigley"
SITENAME = "Ben Quigley"
SITESUBTITLE = "Ben Quigley | Software Developer"
SITEDESCRIPTION = "Ben Quigley homepage"
SITEURL = ""  # Careful, even on local this will ask for CSS etc from this URL
ROBOTS = "index, follow"
MAIN_MENU = True

PATH = "content"

TIMEZONE = "EST"

DEFAULT_LANG = "en"
I18N_TEMPLATES_LANG = "en"
OG_LOCALE = "en_US"
LOCALE = "en_US"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

SITELOGO = "/images/quigley-2022-selfie-square-web.jpg"

# Blogroll
LINKS = (
    ("Github", "https://getpelican.com/"),
    ("LinkedIn", "https://www.linkedin.com/in/BenjaminQuigley/"),
)

# Social widget
SOCIAL = (
    ("github", "https://github.com/BenQuigley"),
    ("linkedin", "https://LinkedIn.com/in/BenjaminQuigley"),
    ("rss", "/blog/feeds/all.atom.xml"),
)

DEFAULT_PAGINATION = 15

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = "themes/Flex"
PLUGIN_PATHS = ["./pelican-plugins"]

TYPOGRIFY = True

# Flex stuff
THEME_COLOR = "light"  # (either "light" (default) or "dark"): the default theme to use when the user/browser/OS does not override it.
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True  # set to True if you want Flex to auto-detect the user's browser/OS color scheme preference and use the appropriate theme.
THEME_COLOR_ENABLE_USER_OVERRIDE = True
