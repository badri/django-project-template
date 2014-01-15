PIPELINE_COMPILERS = (
  'pipeline.compilers.coffee.CoffeeScriptCompiler',
  'pipeline_compass.compiler.CompassCompiler',
)

PIPELINE_CSS = {
    'colors': {
        'source_filenames': (
          'css/core.css',
          'css/colors/*.css',
          'css/layers.css'
        ),
        'output_filename': 'css/colors.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
}

PIPELINE_JS = {
    'stats': {
        'source_filenames': (
          'js/jquery.js',
          'js/d3.js',
          'js/collections/*.js',
          'js/application.js',
        ),
        'output_filename': 'js/stats.js',
    }
    'quiz': {
        'source_filenames': (
          'js/question.coffee',
        ),
        'output_filename': 'js/quiz.js',
    },
    'quiz-editor': {
        'source_filenames': (
          'js/quiz-editor.coffee',
        ),
        'output_filename': 'js/quiz-editor.js',
    }
}
