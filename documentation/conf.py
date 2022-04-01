# Copyright 2020-2022, MicroEJ Corp. Confidentiality and Intellectual Property. All rights reserved. 
# Information, technical data and tutorials contained in this document are confidential and proprietary under copyright Law of Industrial Smart Software Technology (MicroEJ S.A.) operating under the brand name MicroEJ®. Without written permission from MicroEJ S.A., copying or sending parts of the document or the entire document by any means to third parties is not permitted. Granted authorizations for using parts of the document or the entire document do not mean MicroEJ S.A. gives public full access rights.
# The information contained herein is not warranted to be error-free.
# MicroEJ® and all relative logos are trademarks or registered trademarks of MicroEJ S.A. in France and other Countries.
# Java™ is Sun Microsystems’ trademark for a technology for developing application software and deploying it in cross-platform, networked environments. When it is used in this site without adding the “™” symbol, it includes implementations of the technology by companies other than Sun. Java™, all Java-based marks and all related logos are trademarks or registered trademarks of Sun Microsystems Inc, in the United States and other Countries.
# Other trademarks are proprietary of their respective owners.

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

import microej


project = 'GETTING STARTED STM32L4R9IDISCOVERY'
copyright = '2020-2022, MicroEJ Corp. Confidentiality and Intellectual Property. All rights reserved. Information, technical data and tutorials contained in this document are confidential and proprietary under copyright Law of Industrial Smart Software Technology (MicroEJ S.A.) operating under the brand name MicroEJ®. Without written permission from MicroEJ S.A., copying or sending parts of the document or the entire document by any means to third parties is not permitted. Granted authorizations for using parts of the document or the entire document do not mean MicroEJ S.A. gives public full access rights. The information contained herein is not warranted to be error-free. MicroEJ® and all relative logos are trademarks or registered trademarks of MicroEJ S.A. in France and other Countries. Java™ is Sun Microsystems’ trademark for a technology for developing application software and deploying it in cross-platform, networked environments. When it is used in this site without adding the “™” symbol, it includes implementations of the technology by companies other than Sun. Java™, all Java-based marks and all related logos are trademarks or registered trademarks of Sun Microsystems Inc, in the United States and other Countries. Other trademarks are proprietary of their respective owners.'
author = 'MicroEJ'
release = '1.0'

# This isn't executed on normal builds, but can be used to build multiple doc
# sets from this common source. See the ``microej.py`` extension for more
# information.
if microej.can_build_independent_docs():
    project_name = microej.get_project_name()
    if project_name:
        project = project_name

extensions = [
    'microej',
    'sphinx.ext.graphviz',
]

templates_path = ['_templates']
html_theme_path = ['_themes']
master_doc = 'index'

# Generic options
exclude_patterns = [
    '_build',
    '_tools',
    'README.rst',
    'section*.rst',
    '**/section*.rst',
]

# HTML theme options
html_theme = 'microej'
html_logo = '_themes/microej/static/logo-microej-white.png'
html_favicon = '_themes/microej/static/favicon-16x16.png'
html_theme_options = {
    'logo_only': True,
    'collapse_navigation': False,
}
html_show_sphinx = False

# remove headers permalinks
html_add_permalinks = ''

# This is required because the version of the Read the Docs Sphinx theme the
# microej theme was forked from does not support the HTML5 writer used by
# default by Sphinx 2+
html4_writer = True

# The default Sphinx HTML title includes the release number and some other
# unwanted bits.
html_title = project

# LaTeX customizations
latex_elements = {
    'preamble': r'\usepackage{microej}',
    'figure_align': 'H',
    'extraclassoptions': 'oneside',
    #'sphinxsetup': 'inlineliteralwraps=true, verbatimwithframe=true',
}
latex_additional_files = ['microej.sty']
latex_logo = '_themes/microej/static/mascot.pdf'

# This is defined in the theme, but the LaTeX builder does not honor the theme
# setting for pygments. This is the same style class used by the HTML builder.
pygments_style = 'microej.MicroEJStyle'
