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
# from SignUp import Signup
# from Welcome import Welcome
# from Login import Login
# from NewPost import Newpost
# from Blog import Blog
# from SpecificPost import SpecificPost
# from LogOut import Logout
# from Test import Test
# from Editpost import Editpost
# from DeletePost import DeletePost

from Home import Home
from Login import Login
from Newnote import Newnote
from Notes import Notes
from Delete import Delete
from Pw import Pw
from Clear import Clear
from Logout import Logout

# app = webapp2.WSGIApplication([('/blog', Blog),
#                                (r'/blog/(\d+)', SpecificPost),
#                                ('/blog/newpost', Newpost),
#                                (r'/blog/editpost/(\d+)', Editpost),
#                                ('/blog/signup', Signup),
#                                ('/welcome', Welcome),
#                                ('/blog/login', Login),
#                                ('/blog/logout',Logout),
#                                (r'/blog/delete/(\d+)', DeletePost),
#                                ('/test', Test),
#                                (r'/blog/test/(\d+)', Test)],
#                                 debug=True)

app = webapp2.WSGIApplication([('/', Home),
                               ('/newnote', Newnote),
                               ('/notes', Notes),
                               ('/delete', Delete),
                               ('/setps', Pw),
                               ('/clear', Clear),
                               ('/login', Login),
                               ('/logout', Logout)],
                              debug=True)
