{"filter":false,"title":"views.py","tooltip":"/expenses/views.py","undoManager":{"mark":50,"position":50,"stack":[[{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":2}],[{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest",""],"id":3}],[{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":4}],[{"start":{"row":3,"column":0},"end":{"row":6,"column":40},"action":"insert","lines":["from rest_framework import generics, mixins, permissions, viewsets","from rest_framework.authentication import SessionAuthentication","from rest_framework.response import Response","from rest_framework.views import APIView"],"id":5}],[{"start":{"row":6,"column":40},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":6}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":2},"action":"insert","lines":["# "],"id":7},{"start":{"row":4,"column":0},"end":{"row":4,"column":2},"action":"insert","lines":["# "]},{"start":{"row":5,"column":0},"end":{"row":5,"column":2},"action":"insert","lines":["# "]},{"start":{"row":6,"column":0},"end":{"row":6,"column":2},"action":"insert","lines":["# "]}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":1},"action":"insert","lines":["d"],"id":8},{"start":{"row":10,"column":1},"end":{"row":10,"column":2},"action":"insert","lines":["e"]},{"start":{"row":10,"column":2},"end":{"row":10,"column":3},"action":"insert","lines":["f"]}],[{"start":{"row":10,"column":3},"end":{"row":10,"column":4},"action":"insert","lines":[" "],"id":9}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"remove","lines":["def "],"id":10}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":1},"action":"insert","lines":["c"],"id":11}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":1},"action":"remove","lines":["c"],"id":12}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":1},"action":"insert","lines":["c"],"id":13},{"start":{"row":10,"column":1},"end":{"row":10,"column":2},"action":"insert","lines":["l"]},{"start":{"row":10,"column":2},"end":{"row":10,"column":3},"action":"insert","lines":["a"]},{"start":{"row":10,"column":3},"end":{"row":10,"column":4},"action":"insert","lines":["s"]},{"start":{"row":10,"column":4},"end":{"row":10,"column":5},"action":"insert","lines":["s"]}],[{"start":{"row":10,"column":5},"end":{"row":10,"column":6},"action":"insert","lines":[" "],"id":14}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":2},"action":"remove","lines":["# "],"id":15},{"start":{"row":4,"column":0},"end":{"row":4,"column":2},"action":"remove","lines":["# "]},{"start":{"row":5,"column":0},"end":{"row":5,"column":2},"action":"remove","lines":["# "]},{"start":{"row":6,"column":0},"end":{"row":6,"column":2},"action":"remove","lines":["# "]}],[{"start":{"row":10,"column":6},"end":{"row":10,"column":7},"action":"insert","lines":["S"],"id":16}],[{"start":{"row":10,"column":6},"end":{"row":10,"column":7},"action":"remove","lines":["S"],"id":17}],[{"start":{"row":10,"column":6},"end":{"row":10,"column":7},"action":"insert","lines":["S"],"id":18},{"start":{"row":10,"column":7},"end":{"row":10,"column":8},"action":"insert","lines":["p"]},{"start":{"row":10,"column":8},"end":{"row":10,"column":9},"action":"insert","lines":["e"]},{"start":{"row":10,"column":9},"end":{"row":10,"column":10},"action":"insert","lines":["n"]},{"start":{"row":10,"column":10},"end":{"row":10,"column":11},"action":"insert","lines":["t"]}],[{"start":{"row":10,"column":11},"end":{"row":10,"column":12},"action":"insert","lines":["V"],"id":19},{"start":{"row":10,"column":12},"end":{"row":10,"column":13},"action":"insert","lines":["i"]},{"start":{"row":10,"column":13},"end":{"row":10,"column":14},"action":"insert","lines":["e"]},{"start":{"row":10,"column":14},"end":{"row":10,"column":15},"action":"insert","lines":["w"]}],[{"start":{"row":10,"column":15},"end":{"row":10,"column":16},"action":"insert","lines":[" "],"id":20}],[{"start":{"row":10,"column":15},"end":{"row":10,"column":16},"action":"remove","lines":[" "],"id":21}],[{"start":{"row":10,"column":15},"end":{"row":10,"column":17},"action":"insert","lines":["()"],"id":22}],[{"start":{"row":10,"column":16},"end":{"row":10,"column":17},"action":"insert","lines":["g"],"id":23},{"start":{"row":10,"column":17},"end":{"row":10,"column":18},"action":"insert","lines":["e"]},{"start":{"row":10,"column":18},"end":{"row":10,"column":19},"action":"insert","lines":["n"]},{"start":{"row":10,"column":19},"end":{"row":10,"column":20},"action":"insert","lines":["e"]},{"start":{"row":10,"column":20},"end":{"row":10,"column":21},"action":"insert","lines":["r"]},{"start":{"row":10,"column":21},"end":{"row":10,"column":22},"action":"insert","lines":["i"]},{"start":{"row":10,"column":22},"end":{"row":10,"column":23},"action":"insert","lines":["c"]},{"start":{"row":10,"column":23},"end":{"row":10,"column":24},"action":"insert","lines":["s"]},{"start":{"row":10,"column":24},"end":{"row":10,"column":25},"action":"insert","lines":["."]}],[{"start":{"row":10,"column":26},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":24}],[{"start":{"row":11,"column":0},"end":{"row":14,"column":38},"action":"insert","lines":["class UserList(generics.ListCreateAPIView):","    queryset = User.objects.all()","    serializer_class = UserSerializer","    permission_classes = [IsAdminUser]"],"id":25}],[{"start":{"row":11,"column":6},"end":{"row":11,"column":14},"action":"remove","lines":["UserList"],"id":26},{"start":{"row":11,"column":6},"end":{"row":11,"column":15},"action":"insert","lines":["SpentView"]}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":26},"action":"remove","lines":["class SpentView(generics.)"],"id":27},{"start":{"row":9,"column":0},"end":{"row":10,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":6,"column":40},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":28},{"start":{"row":7,"column":0},"end":{"row":8,"column":0},"action":"insert","lines":["",""]},{"start":{"row":8,"column":0},"end":{"row":8,"column":1},"action":"insert","lines":["f"]},{"start":{"row":8,"column":1},"end":{"row":8,"column":2},"action":"insert","lines":["r"]},{"start":{"row":8,"column":2},"end":{"row":8,"column":3},"action":"insert","lines":["o"]},{"start":{"row":8,"column":3},"end":{"row":8,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":8,"column":4},"end":{"row":8,"column":5},"action":"insert","lines":[" "],"id":29},{"start":{"row":8,"column":5},"end":{"row":8,"column":6},"action":"insert","lines":["e"]},{"start":{"row":8,"column":6},"end":{"row":8,"column":7},"action":"insert","lines":["x"]},{"start":{"row":8,"column":7},"end":{"row":8,"column":8},"action":"insert","lines":["p"]},{"start":{"row":8,"column":8},"end":{"row":8,"column":9},"action":"insert","lines":["e"]},{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"insert","lines":["n"]}],[{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"insert","lines":["s"],"id":30},{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"insert","lines":["e"]},{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"insert","lines":["s"]},{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"insert","lines":["."]}],[{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"insert","lines":["m"],"id":31},{"start":{"row":8,"column":15},"end":{"row":8,"column":16},"action":"insert","lines":["o"]},{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"insert","lines":["d"]},{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"insert","lines":["e"]},{"start":{"row":8,"column":18},"end":{"row":8,"column":19},"action":"insert","lines":["l"]},{"start":{"row":8,"column":19},"end":{"row":8,"column":20},"action":"insert","lines":["s"]}],[{"start":{"row":8,"column":20},"end":{"row":8,"column":21},"action":"insert","lines":[" "],"id":32},{"start":{"row":8,"column":21},"end":{"row":8,"column":22},"action":"insert","lines":["i"]},{"start":{"row":8,"column":22},"end":{"row":8,"column":23},"action":"insert","lines":["m"]},{"start":{"row":8,"column":23},"end":{"row":8,"column":24},"action":"insert","lines":["p"]},{"start":{"row":8,"column":24},"end":{"row":8,"column":25},"action":"insert","lines":["o"]},{"start":{"row":8,"column":25},"end":{"row":8,"column":26},"action":"insert","lines":["r"]},{"start":{"row":8,"column":26},"end":{"row":8,"column":27},"action":"insert","lines":["t"]}],[{"start":{"row":8,"column":27},"end":{"row":8,"column":28},"action":"insert","lines":[" "],"id":33},{"start":{"row":8,"column":28},"end":{"row":8,"column":29},"action":"insert","lines":["S"]}],[{"start":{"row":8,"column":28},"end":{"row":8,"column":29},"action":"remove","lines":["S"],"id":34},{"start":{"row":8,"column":28},"end":{"row":8,"column":33},"action":"insert","lines":["Spent"]}],[{"start":{"row":13,"column":15},"end":{"row":13,"column":19},"action":"remove","lines":["User"],"id":35},{"start":{"row":13,"column":15},"end":{"row":13,"column":16},"action":"insert","lines":["S"]},{"start":{"row":13,"column":16},"end":{"row":13,"column":17},"action":"insert","lines":["p"]},{"start":{"row":13,"column":17},"end":{"row":13,"column":18},"action":"insert","lines":["e"]},{"start":{"row":13,"column":18},"end":{"row":13,"column":19},"action":"insert","lines":["n"]},{"start":{"row":13,"column":19},"end":{"row":13,"column":20},"action":"insert","lines":["t"]}],[{"start":{"row":8,"column":33},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":36},{"start":{"row":9,"column":0},"end":{"row":9,"column":1},"action":"insert","lines":["f"]},{"start":{"row":9,"column":1},"end":{"row":9,"column":2},"action":"insert","lines":["r"]},{"start":{"row":9,"column":2},"end":{"row":9,"column":3},"action":"insert","lines":["o"]},{"start":{"row":9,"column":3},"end":{"row":9,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":9,"column":4},"end":{"row":9,"column":5},"action":"insert","lines":[" "],"id":37},{"start":{"row":9,"column":5},"end":{"row":9,"column":6},"action":"insert","lines":["e"]}],[{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"remove","lines":["s"],"id":38},{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"remove","lines":["e"]},{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"remove","lines":["s"]},{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"remove","lines":["n"]},{"start":{"row":8,"column":8},"end":{"row":8,"column":9},"action":"remove","lines":["e"]},{"start":{"row":8,"column":7},"end":{"row":8,"column":8},"action":"remove","lines":["p"]},{"start":{"row":8,"column":6},"end":{"row":8,"column":7},"action":"remove","lines":["x"]},{"start":{"row":8,"column":5},"end":{"row":8,"column":6},"action":"remove","lines":["e"]}],[{"start":{"row":9,"column":5},"end":{"row":9,"column":6},"action":"remove","lines":["e"],"id":39}],[{"start":{"row":9,"column":5},"end":{"row":9,"column":6},"action":"insert","lines":["."],"id":40},{"start":{"row":9,"column":6},"end":{"row":9,"column":7},"action":"insert","lines":["s"]},{"start":{"row":9,"column":7},"end":{"row":9,"column":8},"action":"insert","lines":["e"]},{"start":{"row":9,"column":8},"end":{"row":9,"column":9},"action":"insert","lines":["r"]},{"start":{"row":9,"column":9},"end":{"row":9,"column":10},"action":"insert","lines":["i"]},{"start":{"row":9,"column":10},"end":{"row":9,"column":11},"action":"insert","lines":["a"]}],[{"start":{"row":9,"column":6},"end":{"row":9,"column":11},"action":"remove","lines":["seria"],"id":41},{"start":{"row":9,"column":6},"end":{"row":9,"column":17},"action":"insert","lines":["serializers"]}],[{"start":{"row":9,"column":17},"end":{"row":9,"column":18},"action":"insert","lines":[" "],"id":42},{"start":{"row":9,"column":18},"end":{"row":9,"column":19},"action":"insert","lines":["i"]},{"start":{"row":9,"column":19},"end":{"row":9,"column":20},"action":"insert","lines":["m"]},{"start":{"row":9,"column":20},"end":{"row":9,"column":21},"action":"insert","lines":["p"]},{"start":{"row":9,"column":21},"end":{"row":9,"column":22},"action":"insert","lines":["o"]},{"start":{"row":9,"column":22},"end":{"row":9,"column":23},"action":"insert","lines":["r"]},{"start":{"row":9,"column":23},"end":{"row":9,"column":24},"action":"insert","lines":["t"]}],[{"start":{"row":9,"column":24},"end":{"row":9,"column":25},"action":"insert","lines":[" "],"id":43},{"start":{"row":9,"column":25},"end":{"row":9,"column":26},"action":"insert","lines":["S"]},{"start":{"row":9,"column":26},"end":{"row":9,"column":27},"action":"insert","lines":["p"]},{"start":{"row":9,"column":27},"end":{"row":9,"column":28},"action":"insert","lines":["e"]},{"start":{"row":9,"column":28},"end":{"row":9,"column":29},"action":"insert","lines":["n"]}],[{"start":{"row":9,"column":29},"end":{"row":9,"column":30},"action":"insert","lines":["s"],"id":44},{"start":{"row":9,"column":30},"end":{"row":9,"column":31},"action":"insert","lines":["e"]}],[{"start":{"row":9,"column":30},"end":{"row":9,"column":31},"action":"remove","lines":["e"],"id":45},{"start":{"row":9,"column":29},"end":{"row":9,"column":30},"action":"remove","lines":["s"]}],[{"start":{"row":9,"column":29},"end":{"row":9,"column":30},"action":"insert","lines":["t"],"id":46},{"start":{"row":9,"column":30},"end":{"row":9,"column":31},"action":"insert","lines":["s"]},{"start":{"row":9,"column":31},"end":{"row":9,"column":32},"action":"insert","lines":["e"]}],[{"start":{"row":9,"column":31},"end":{"row":9,"column":32},"action":"remove","lines":["e"],"id":47},{"start":{"row":9,"column":30},"end":{"row":9,"column":31},"action":"remove","lines":["s"]}],[{"start":{"row":9,"column":30},"end":{"row":9,"column":31},"action":"insert","lines":["S"],"id":48},{"start":{"row":9,"column":31},"end":{"row":9,"column":32},"action":"insert","lines":["e"]}],[{"start":{"row":9,"column":25},"end":{"row":9,"column":32},"action":"remove","lines":["SpentSe"],"id":49},{"start":{"row":9,"column":25},"end":{"row":9,"column":40},"action":"insert","lines":["SpentSerializer"]}],[{"start":{"row":15,"column":23},"end":{"row":15,"column":37},"action":"remove","lines":["UserSerializer"],"id":50},{"start":{"row":15,"column":23},"end":{"row":15,"column":24},"action":"insert","lines":["S"]},{"start":{"row":15,"column":24},"end":{"row":15,"column":25},"action":"insert","lines":["p"]},{"start":{"row":15,"column":25},"end":{"row":15,"column":26},"action":"insert","lines":["e"]},{"start":{"row":15,"column":26},"end":{"row":15,"column":27},"action":"insert","lines":["n"]},{"start":{"row":15,"column":27},"end":{"row":15,"column":28},"action":"insert","lines":["t"]}],[{"start":{"row":15,"column":23},"end":{"row":15,"column":28},"action":"remove","lines":["Spent"],"id":51},{"start":{"row":15,"column":23},"end":{"row":15,"column":38},"action":"insert","lines":["SpentSerializer"]}],[{"start":{"row":16,"column":0},"end":{"row":16,"column":38},"action":"remove","lines":["    permission_classes = [IsAdminUser]"],"id":52},{"start":{"row":15,"column":38},"end":{"row":16,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":15,"column":38},"end":{"row":15,"column":38},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1584682435144,"hash":"6fad2e6565b8a5c6cbe4422039869b12736eda39"}