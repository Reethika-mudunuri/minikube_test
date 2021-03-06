from kubernetes import client, config


class Pod(object):

    def __init__(self, name, images, labels, recent_start_time):
        self.name = name
        self.images = images
        self.labels = labels
        self.recent_start_time = recent_start_time


class PodApi(object):

    def __init__(self):
        config.load_kube_config()
        v1 = client.CoreV1Api()
        self.pods = v1.list_pod_for_all_namespaces(watch=False)

    def __get_images(self, pod):
        """
        Gets the images from the pods
        """
        images = []
        for container in pod.spec.containers:
            images.append(container.image)
        return images

    def __get_labels(self, pod):
        """
        Gets the images from the pods
        """
        return pod.metadata.labels

    def __get_start_time(self, pod):
        """
        Gets the images from the pods
        """
        return pod.status.start_time

    def build_pod_details(self):
        pod_details = []
        for pod in self.pods.items:
            name = pod.metadata.name
            images = self.__get_images(pod=pod)
            labels = self.__get_labels(pod=pod)
            recent_start_time = self.__get_start_time(pod=pod)
            pod_details.append(
                Pod(name=name,
                    images=images,
                    labels=labels,
                    recent_start_time=recent_start_time))

        return pod_details
