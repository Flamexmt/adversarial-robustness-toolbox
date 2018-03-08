from __future__ import absolute_import, division, print_function

from keras import backend as k
from keras.engine import Layer


class BoundedReLU(Layer):
    """Bounded Rectified Linear Unit.
    `f(x) = alpha * x for x < 0`,
    `f(x) = x for x >= 0`,
    `f(x) = max_value for x > max_value.`
    """
    def __init__(self, alpha=0., max_value=1., **kwargs):
        """

        :param alpha: float >= 0, negative slope coefficient for leaky ReLU
        :param max_value: float, > 0, maximal value of the function
        :param kwargs: input_shape: when using this layer as the first layer in a model.
        """
        assert max_value > 0., "max_value must be positive"
        super(BoundedReLU, self).__init__(**kwargs)
        self.supports_masking = True
        self.alpha = k.cast_to_floatx(alpha)
        self.max_value = k.cast_to_floatx(max_value)

    def call(self, inputs):
        return k.relu(inputs, alpha=self.alpha, max_value=self.max_value)

    def get_config(self):
        """Get the parameters of the object"""
        config = {'alpha': self.alpha, 'max_value': self.max_value}
        base_config = super(BoundedReLU, self).get_config()
        return dict(list(base_config.items()) + list(config.items()))
