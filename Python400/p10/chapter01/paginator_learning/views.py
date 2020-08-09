from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Student
# Create your views here.


def student_list(request, page=1):

    def get_range_by_page_and_max_page(current_page, max_page, length=10):
        """
        generate range for pager
        :param current_page: number of current page
        :param max_page: num_pages of paginator
        :param length: length of pager
        :return: seq
        """
        # if max_page less than length,
        # return [1, max_page].
        if max_page < length:
            return range(1, max_page+1)

        # if current_page grater than or equal 1 and less than or equal 1/2 length,
        # return [1, length].
        if 1 <= current_page <= length // 2:
            return range(1, length + 1)

        # if current_page grater than or equal max_page sub 1/2 length and less than or equal max_page,
        # return [max_page - length, max_page]
        if (max_page - length // 2) <= current_page <= max_page:
            return range(max_page - length, max_page + 1)

        min_ = current_page - length // 2
        max_ = current_page + length // 2
        return range(min_, max_+1)


    # initialize paginator
    students = Student.objects.all()
    paginator = Paginator(students, 50)

    # get page
    page = paginator.get_page(page)

    # render
    return render(
        request,
        'paginator_learning/students.html',
        context={
            'students': page.object_list,
            'page': page,
            'paginator': paginator,
            'range': get_range_by_page_and_max_page(page.number, paginator.num_pages)
        }
    )
