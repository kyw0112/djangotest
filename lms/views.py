from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

@api_view(["POST"])
@permission_classes([AllowAny])
    data = request.data or {}
        return Response({"detail": "username and password required"}, status=400)
        return Response({"detail": "User exists"}, status=400)
    return Response({"id": user.id, "username": user.username})

@api_view(["POST"])
@permission_classes([AllowAny])
    data = request.data or {}
        return Response({"detail": "Invalid credentials"}, status=400)
    return Response({"detail": "logged in"})
@api_view(["GET"])
@permission_classes([IsAuthenticated])
    return Response({"id": user.id, "username": user.username})
@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
    data = request.data or {}
    return Response({"detail": "updated"})
@api_view(["POST", "GET"])
@permission_classes([IsAuthenticated])
        data = request.data or {}
        return Response({"id": student.id, "name": student.name})
        return Response({"results": data})
    return Response({"detail": "Method not allowed"}, status=405)
@api_view(["GET", "PATCH", "DELETE"])
@permission_classes([IsAuthenticated])
        return Response({"detail": "Not found"}, status=404)
        return Response({"id": student.id, "name": student.name})
        data = request.data or {}
        return Response({"detail": "updated"})
        return Response({"detail": "deleted"})
    return Response({"detail": "Method not allowed"}, status=405)
@api_view(["POST"])
@permission_classes([IsAuthenticated])
        data = request.data or {}
            return Response({"detail": "Student not found"}, status=404)
        return Response({"id": cur.id, "title": cur.title})
    return Response({"detail": "Method not allowed"}, status=405)
@api_view(["GET"])
@permission_classes([IsAuthenticated])
    return Response({"results": data})
@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
        return Response({"detail": "Not found"}, status=404)
        data = request.data or {}
        return Response({"detail": "updated"})
    return Response({"detail": "Method not allowed"}, status=405)
@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
        return Response({"detail": "Not found"}, status=404)
        data = request.data or {}
        return Response({"detail": "updated"})
    return Response({"detail": "Method not allowed"}, status=405)

@csrf_exempt
@api_view(["POST"])
@permission_classes([IsAuthenticated])
    data = request.data or {}
        return Response({"detail": "Curriculum not found"}, status=404)
    return Response({"id": lesson.id})
@api_view(["GET"])
@permission_classes([IsAuthenticated])
    return Response({"results": data})
@api_view(["GET"])
@permission_classes([IsAuthenticated])
    return Response({"amount": total})
@api_view(["POST"])
@permission_classes([IsAuthenticated])
    return Response({"detail": "invoice sent"})
@api_view(["GET"])
@permission_classes([IsAuthenticated])
    return Response({"results": data})
@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
        return Response({"detail": "Not found"}, status=404)
        data = request.data or {}
        return Response({"detail": "updated"})
    return Response({"detail": "Method not allowed"}, status=405)
@api_view(["POST"])
@permission_classes([IsAuthenticated])
    return Response({"detail": "report draft created"})
@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
    return Response({"detail": "report updated"})
@api_view(["POST"])
@permission_classes([IsAuthenticated])
    return Response({"detail": "report sent"})

@api_view(["GET"])
@permission_classes([IsAuthenticated])
    return Response({"results": []})
@api_view(["GET"])
@permission_classes([IsAuthenticated])
    return Response({"todos": []})
        student = Student.objects.get(id=id, teacher=request.user)
    except Student.DoesNotExist:
        return JsonResponse({"detail": "Not found"}, status=404)

    if request.method == "GET":
        return JsonResponse({"id": student.id, "name": student.name})
    elif request.method == "PATCH":
        data = json.loads(request.body or "{}")
        student.name = data.get("name", student.name)
        student.contact = data.get("contact", student.contact)
        student.class_name = data.get("class_name", student.class_name)
        student.parent_email = data.get("parent_email", student.parent_email)
        student.save()
        return JsonResponse({"detail": "updated"})
    elif request.method == "DELETE":
        student.delete()
        return JsonResponse({"detail": "deleted"})
    return JsonResponse({"detail": "Method not allowed"}, status=405)


@csrf_exempt
@login_required
def curriculum_collection(request):
    if request.method == "POST":
        data = json.loads(request.body or "{}")
        try:
            student = Student.objects.get(id=data.get("student_id"), teacher=request.user)
        except Student.DoesNotExist:
            return JsonResponse({"detail": "Student not found"}, status=404)
        cur = Curriculum.objects.create(
            student=student,
            title=data.get("title", ""),
            target_mastery=data.get("target_mastery", 0),
            description=data.get("description", ""),
        )
        return JsonResponse({"id": cur.id, "title": cur.title})
    return JsonResponse({"detail": "Method not allowed"}, status=405)


@login_required
def curriculum_by_student(request, student_id):
    cur_list = Curriculum.objects.filter(student__id=student_id, student__teacher=request.user)
    data = [{"id": c.id, "title": c.title, "target_mastery": c.target_mastery} for c in cur_list]
    return JsonResponse({"results": data})


@csrf_exempt
@login_required
def curriculum_detail(request, id):
    try:
        cur = Curriculum.objects.get(id=id, student__teacher=request.user)
    except Curriculum.DoesNotExist:
        return JsonResponse({"detail": "Not found"}, status=404)
    if request.method == "PATCH":
        data = json.loads(request.body or "{}")
        cur.title = data.get("title", cur.title)
        cur.target_mastery = data.get("target_mastery", cur.target_mastery)
        cur.description = data.get("description", cur.description)
        cur.save()
        return JsonResponse({"detail": "updated"})
    return JsonResponse({"detail": "Method not allowed"}, status=405)


@csrf_exempt
@login_required
def progress_update(request, id):
    try:
        lesson = Lesson.objects.get(id=id, curriculum__student__teacher=request.user)
    except Lesson.DoesNotExist:
        return JsonResponse({"detail": "Not found"}, status=404)
    if request.method == "PATCH":
        data = json.loads(request.body or "{}")
        lesson.progress = data.get("progress", lesson.progress)
        lesson.save()
        return JsonResponse({"detail": "updated"})
    return JsonResponse({"detail": "Method not allowed"}, status=405)


@csrf_exempt
@login_required
def session_record(request):
    if request.method != "POST":
        return JsonResponse({"detail": "Method not allowed"}, status=405)
    data = json.loads(request.body or "{}")
    try:
        curriculum = Curriculum.objects.get(id=data.get("curriculum_id"), student__teacher=request.user)
    except Curriculum.DoesNotExist:
        return JsonResponse({"detail": "Curriculum not found"}, status=404)
    lesson = Lesson.objects.create(
        curriculum=curriculum,
        date=data.get("date"),
        duration_hours=data.get("duration_hours", 1),
        progress=data.get("progress", 0),
    )
    Attendance.objects.create(
        lesson=lesson,
        student=curriculum.student,
        present=data.get("present", True),
    )
    return JsonResponse({"id": lesson.id})


@login_required
def session_calendar(request):
    student_id = request.GET.get("student_id")
    lessons = Lesson.objects.filter(curriculum__student__id=student_id, curriculum__student__teacher=request.user)
    data = [
        {
            "date": l.date,
            "progress": float(l.progress),
        }
        for l in lessons
    ]
    return JsonResponse({"results": data})


@login_required
def invoice_preview(request):
    student_id = request.GET.get("student_id")
    # This is a placeholder calculation
    total = Lesson.objects.filter(curriculum__student__id=student_id, curriculum__student__teacher=request.user).count() * 100
    return JsonResponse({"amount": total})


@csrf_exempt
@login_required
def invoice_send(request):
    if request.method != "POST":
        return JsonResponse({"detail": "Method not allowed"}, status=405)
    return JsonResponse({"detail": "invoice sent"})


@login_required
def invoice_history(request):
    invoices = Invoice.objects.filter(student__teacher=request.user)
    data = [
        {"id": inv.id, "month": inv.month, "amount": float(inv.amount), "paid": inv.paid}
        for inv in invoices
    ]
    return JsonResponse({"results": data})


@csrf_exempt
@login_required
def invoice_update(request, id):
    try:
        inv = Invoice.objects.get(id=id, student__teacher=request.user)
    except Invoice.DoesNotExist:
        return JsonResponse({"detail": "Not found"}, status=404)
    if request.method == "PATCH":
        data = json.loads(request.body or "{}")
        inv.paid = data.get("paid", inv.paid)
        inv.save()
        return JsonResponse({"detail": "updated"})
    return JsonResponse({"detail": "Method not allowed"}, status=405)


@csrf_exempt
@login_required
def report_generate(request):
    if request.method != "POST":
        return JsonResponse({"detail": "Method not allowed"}, status=405)
    return JsonResponse({"detail": "report draft created"})


@csrf_exempt
@login_required
def report_update(request, id):
    if request.method != "PATCH":
        return JsonResponse({"detail": "Method not allowed"}, status=405)
    return JsonResponse({"detail": "report updated"})


@csrf_exempt
@login_required
def report_send(request):
    if request.method != "POST":
        return JsonResponse({"detail": "Method not allowed"}, status=405)
    return JsonResponse({"detail": "report sent"})


@login_required
def report_history(request):
    student_id = request.GET.get("student_id")
    return JsonResponse({"results": []})


@login_required
def notifications_todo(request):
    return JsonResponse({"todos": []})
