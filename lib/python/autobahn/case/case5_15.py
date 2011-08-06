###############################################################################
##
##  Copyright 2011 Tavendo GmbH
##
##  Licensed under the Apache License, Version 2.0 (the "License");
##  you may not use this file except in compliance with the License.
##  You may obtain a copy of the License at
##
##      http://www.apache.org/licenses/LICENSE-2.0
##
##  Unless required by applicable law or agreed to in writing, software
##  distributed under the License is distributed on an "AS IS" BASIS,
##  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
##  See the License for the specific language governing permissions and
##  limitations under the License.
##
###############################################################################

from case import Case

class Case5_15(Case):

   ID = "5.15"

   DESCRIPTION = """Send text Message fragmented into 2 fragments, then Continuation Frame with FIN = false where there is nothing to continue, then unfragmented Text Message, all sent in one chop."""

   EXPECTATION = """The connection is failed immediately, since there is no message to continue."""

   def onOpen(self):
      self.expected = [("failedByMe", False)]
      self.p.sendFrame(opcode = 1, fin = False, payload = "fragment1")
      self.p.sendFrame(opcode = 0, fin = True, payload = "fragment2")
      self.p.sendFrame(opcode = 0, fin = False, payload = "fragment3")
      self.p.sendFrame(opcode = 1, fin = True, payload = "fragment4")
      self.p.killAfter(1)
