# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import webapp2
from Login import Login
from Newnote import Newnote
from Notes import Notes
from Delete import Delete
from Pw import Pw
from Clear import Clear
from Logout import Logout
from SpecificNote import SpecificNote



app = webapp2.WSGIApplication([('/', Login),
                               ('/newnote', Newnote),
                               ('/notes', Notes),
                               (r'/note/(\d+)', SpecificNote),
                               ('/delete', Delete),
                               ('/setps', Pw),
                               ('/clear', Clear),
                               ('/login', Login),
                               ('/logout', Logout)],
                              debug=True)
