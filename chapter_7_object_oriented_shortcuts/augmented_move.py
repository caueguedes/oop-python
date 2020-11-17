import shutil
import os.path


def augmented_move(target_folder, *filenames, verbose=False, **specific):
    """Move all filenames into the target_folder, allowing
    specific treatment of certain files."""

    def print_verbose(message, filename):
        """print the message only if verbose is enabled"""
        if verbose:
            print(message.format(filename))

    for filename in filenames:
        target_path = os.path.join(target_folder, filename)
        if filename in specific:
            if specific[filename] == "ignore":
                print_verbose("Ignoring {0}", filename)
            elif specific[filename] == "copy":
                print_verbose("Copying {0}", filename)
                shutil.copyfile(filename, target_path)

        else:
            print_verbose("Moving {0}", filename)
            shutil.move(filename, target_path)


augmented_move("move_here", "one", "two")
augmented_move("move_here", "three", verbose=True)  # Moving three
augmented_move("move_here", "four", "five", "six", four="copy", five="ignore")

augmented_move("move_here", "seven", "eight", "nine", seven="copy", verbose=True, eight="ignore")
#  copying seven
#  ignoring eight
#  moving nine

