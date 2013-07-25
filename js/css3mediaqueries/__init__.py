from fanstatic import Library, Resource
import fanstatic

library = Library('css3mediaqueries', 'resources')


def lte_ie8_renderer(url):
    inner = fanstatic.core.render_js(url)
    return "<!--[if lte IE 8 ]>%s<![endif]-->" % inner


css3mediaqueries = Resource(
    library, 'css3-mediaqueries.js',
    bottom=True,
    renderer=lte_ie8_renderer,
)
