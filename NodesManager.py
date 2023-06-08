import dearpygui.dearpygui as dpg

class NodesManager:

    def __init__(self, window):
        self.window = window

    def link(self, first, second):

        first.next_nodes.append(second)

        if (first.out_image_id[0] != -1):
            second.in_image_id = first.out_image_id

        first.update_image()

    def link_callback(self, sender, app_data):
        first_link = app_data[0]
        second_link = app_data[1]

        first_node = -1
        second_node = -1

        for node in self.window.nodes:
            if node.in_id == first_link or node.out_id == first_link:
                first_node = node
                break

        for node in self.window.nodes:
            if node.in_id == second_link or node.out_id == second_link:
                second_node = node
                break

        self.link(first_node, second_node)
        dpg.add_node_link(app_data[0], app_data[1], parent=sender)

    def delink_callback(self, sender, app_data):
        dpg.delete_item(app_data)

    def delete_node(self, sender, app_data):
        nodes_to_delete = dpg.get_selected_nodes(node_editor=self.window.node_editor_id)

        for node_index in nodes_to_delete:
            dpg.delete_item(node_index)

            for node in self.window.nodes:
                if node.id == node_index:
                    self.window.nodes.remove(node)
                    break