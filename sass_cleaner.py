import sublime_plugin, os

class SassCleanerCommand(sublime_plugin.EventListener):
  def on_pre_save(self, view):
    extension = os.path.splitext(view.file_name())[1]

    if extension != '.sass' or view.size() <= 0:
      return

    regions = view.find_all('[;{}]+|\n{3,}$')

    regions.reverse()

    edit = view.begin_edit()

    for region in regions:
      view.erase(edit, region)

    view.end_edit(edit)
