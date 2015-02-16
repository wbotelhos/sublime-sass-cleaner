import sublime_plugin, os

def should_process(view):
  extension = os.path.splitext(view.file_name())[1]

  return extension == '.sass' and view.size() > 0

def get_regions(view):
  regions = view.find_all('[;{}]+|\n{3,}$')

  return regions.reverse()

class SassCleanerCommand(sublime_plugin.EventListener):
  def on_pre_save(self, view):
    if not should_process(view):
      return

    regions = get_regions(view)
    edit    = view.begin_edit()

    for region in regions:
      view.erase(edit, region)

    view.end_edit(edit)

