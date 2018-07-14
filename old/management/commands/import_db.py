from django.core.management.base import BaseCommand, CommandError

from old.models import Laptop, Pc, Printer, Product
from comp_info import models as m

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        product = Product.objects.using('old').all()
        laptop = Laptop.objects.using('old').all()
        pc = Pc.objects.using('old').all()
        printer = Printer.objects.using('old').all()

        # for p in product:
        #     del p.__dict__['_state']
        #     m.Product.objects.create(**p.__dict__)
        obj = [laptop,pc,printer]
        model = [m.Laptop, m.Pc, m.Printer]
        for elem,mod in zip(obj,model):
            for p in elem:
                del p.__dict__['_state']
                id = int(p.__dict__.pop('model_id'))
                intro = mod(**p.__dict__)
                intro.model = m.Product.objects.get(model=id)
                intro.save()
