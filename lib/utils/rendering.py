# coding: utf-8

import os


def render_template(template_name, data):
    print template_name, os.getcwd(), data

    template_path = os.path.join(os.getcwd(), 'app/templates/%s.html.twig' % template_name)

    if not os.path.exists(template_path):
        raise NotImplementedError

    with open(template_path) as f:
        fcontents = f.read().replace('{{ content }}', str(data))

        print '>>>', fcontents

        return fcontents


class render_to(object):

    def __init__(self, template_name='default'):
        self._template_name = template_name

    def __call__(self, controller):
        def wrapper(*args, **kwargs):
            print args, kwargs
            data = controller(*args, **kwargs)
            print '-->', self._template_name
            return render_template(self._template_name, data)
        return wrapper
