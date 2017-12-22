class TovarView(View):
    def get(self, request):
        a = TovarModel.objects.all()
        return render(request, 'order.html', {'a':a})
