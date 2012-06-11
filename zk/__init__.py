from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from controllers.legacy_view import LegacyView
from model import meta, init_model
from zk import forms

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    init_model(engine)
    
    config = Configurator(settings=settings)
    config.add_static_view('static', 'zk:static', cache_max_age=3600)

    config.include('pyramid_formalchemy')
    # Adding the jquery libraries
    config.include('fa.bootstrap')

    config.formalchemy_admin("/admin",
                             models=model,
                             forms=forms,
                             session_factory=meta.Session,
                             view="zk.forms.ModelView")
    
    #config.add_static_view('public', 'public', cache_max_age=3600)
    config.add_route('home', '/pyramid')

    legacy_view = LegacyView(global_config, **settings)
    config.add_notfound_view(view=legacy_view)

    config.scan()
    return config.make_wsgi_app()

