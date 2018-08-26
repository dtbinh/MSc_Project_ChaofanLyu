import os, argparse
import tensorflow as tf

dir = os.path.dirname(os.path.realpath(__file__))

def freeze_graph(model_dir, output_node_names):

    if not tf.gfile.Exists(model_dir):
        raise AssertionError(
            "Export directory doesn't exists. Please specify an export"
            "directory: %s" % model_dir
        )

    if not output_node_names:
        print("You need to supply the name of a node to --output_node_names.")
        return -1
    
    checkpoint = tf.train.get_checkpoint_state(model_dir)
    input_checkpoint = checkpoint.model_checkpoint_path

    absolute_model_dir = "/".join(input_checkpoint.split('/')[:-1])
    output_graph = absolute_model_dir + "/frozen_model.pb"

    clear_devices = True

    #start a session using a temporary fresh graph
    with tf.Session(graph=tf.Graph()) as sess:
        #import the meta graph in the current default graph
        saver =tf.train.import_meta_graph(input_checkpoint + '.meta', clear_devices=clear_devices)

        #restore the weights
        saver.restore(sess, input_checkpoint)

        #export variables to constants
        output_graph_def = tf.graph_util.convert_variables_to_constants(
            sess, #the session is used to retrieve the weights 
            tf.get_default_graph().as_graph_def(), #the graph_def is used to retrieve the nodes
            output_node_names.split(",") #the output node names are used to select the usefull nodes
        )

        #serialize and dump the output graph to the filesystem
        with tf.gfile.GFile(output_graph, "wb") as f:
            f.write(output_graph_def.SerializeToString())
        print("%d in the final graph." % len(output_graph_def.node))

    return output_graph_def

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_dir",  type=str, default="", help="Model folder to export")
    parser.add_argument("--output_node_names", type=str, default="", help="The name of the output nodes, comma separated.")
    args = parser.parse_args()

    freeze_graph(args.model_dir, args.output_node_names)

    
