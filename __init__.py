# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
# flake8: noqa

"""EnCodec neural audio codec."""

__version__ = "0.0.1"

from .model import EncodecModel
from .compress import compress, decompress