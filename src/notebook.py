# https://nbconvert.readthedocs.io/en/latest/nbconvert_library.html
import nbconvert
import nbformat
import nbparameterise
import os


TEMPLATE_PATH       = os.getenv('TEMPLATE_PATH', 'nbconvert/templates')
LATEX_TEMPLATE_PATH = os.getenv('LATEX_TEMPLATE_PATH', f'{TEMPLATE_PATH}/latex')
CUSTOM_TEMPLATE     = os.getenv('LATEX_TEMPLATE', f'{LATEX_TEMPLATE_PATH}/article.tplx')
DEFAULT_TEMPLATE    = 'article.tplx'  # from nbconvert lib on path
NOTEBOOK_VERSION    = int(os.getenv('NOTEBOOK_VERSION', 4))
KERNEL_NAME         = os.getenv('KERNEL_NAME', 'python3')
EXECUTION_TIMEOUT   = os.getenv('EXECUTION_TIMEOUT', 1000)  # TODO - unit?
NOTEBOOK_FILENAME   = os.getenv('NOTEBOOK_FILENAME', 'test.ipynb')
AUTHOR              = os.getenv('AUTHOR', 'No Author')
TITLE               = os.getenv('TITLE', 'No Title')


def _open(notebook_filename=NOTEBOOK_FILENAME):
    with open(notebook_filename) as f:
        return nbformat.read(f, as_version=NOTEBOOK_VERSION)


def _execute(nb, **notebook_params):
    orig_parameters = nbparameterise.extract_parameters(nb)  # extracts parameters from FIRST cell
    replaced_params = nbparameterise.parameter_values(orig_parameters, **notebook_params)
    nb = nbparameterise.replace_definitions(nb, replaced_params)
    ep = nbconvert.preprocessors.ExecutePreprocessor(timeout=EXECUTION_TIMEOUT, kernel_name=KERNEL_NAME)
    ep.preprocess(nb)
    return nb


def _export_pdf(nb, input_cells=True, execution_counts=True, metadata=dict()):
    # Some display options must be customized in the template, such as author,
    # others are coded into the exporter, such as input cell exclusion.
    template_file = _select_template(execution_counts=execution_counts,
                                     input_cells=input_cells,
                                     **metadata)
    pe = nbconvert.PDFExporter(template_file=template_file)
    pe.exclude_input = not input_cells
    bs, _ = pe.from_notebook_node(nb, dict(metadata=metadata))
    return bs


def _select_template(**kwargs):
    return CUSTOM_TEMPLATE if not kwargs['execution_counts'] else DEFAULT_TEMPLATE


def create_pdf(author=AUTHOR, title=TITLE, **notebook_params):
    nb = _open()
    nb = _execute(nb, **notebook_params)
    bs = _export_pdf(nb,
                     input_cells=False,
                     execution_counts=False,
                     metadata=dict(author=author,
                                   title=title))
    return bs
