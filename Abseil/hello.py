from absl import app
from absl import flags

FLAGS = flags.FLAGS
flags.DEFINE_string("name", None, "Your name.")
flags.DEFINE_integer("num_times", 1,
                     "Number of times to print greeting.")

# Require flag.
flags.mark_flag_as_required("name")

def main(argv):
    del argv # Unused.
    for i in range(0, FLAGS.num_times):
        print("Hello, {}!".format(FLAGS.name))

if __name__ == "__main__":
    app.run(main)              
