from django.shortcuts import render
from django.core.cache import caches
import time


def non_cached_view(request):
    return render(
        request,
        "non_cached_page.html",
        {
            "cached": "No (Non Cached Page)",
        },
    )


def per_view_cached_view(request):
    cache = caches["localmemory"]
    data = cache.get("per_view_cached_data")

    if not data:
        time.sleep(2)  # симулируем долгую операцию
        data = "Generated fresh content (localmemory cache)"
        cache.set("per_view_cached_data", data, timeout=60)

    return render(
        request,
        "per_view_cached_page.html",
        {
            "cached": "Yes (LocalMemory Cached Page)",
            "data": data,
        },
    )


def cached_view(request):
    cache = caches["default"]  # Memcached
    data = cache.get("cached_page_data")

    if not data:
        time.sleep(2)
        data = "Generated fresh content (memcached)"
        cache.set("cached_page_data", data, timeout=60)

    return render(
        request,
        "cached_page.html",
        {
            "cached": "Yes (Memcached Cached Page)",
            "data": data,
        },
    )


def filesystem_cached_view(request):
    cache = caches["filesystem"]
    data = cache.get("filesystem_cached_data")

    if not data:
        time.sleep(2)
        data = "Generated fresh content (filesystem cache)"
        cache.set("filesystem_cached_data", data, timeout=60)

    return render(
        request,
        "filesystem_cached_page.html",
        {
            "cached": "Yes (Filesystem Cached Page)",
            "data": data,
        },
    )


def database_cached_view(request):
    cache = caches["database"]
    data = cache.get("database_cached_data")

    if not data:
        time.sleep(2)
        data = "Generated fresh content (database cache)"
        cache.set("database_cached_data", data, timeout=60)

    return render(
        request,
        "database_cached_page.html",
        {
            "cached": "Yes (Database Cached Page)",
            "data": data,
        },
    )


def dummy_cached_view(request):
    cache = caches["dummy"]
    data = cache.get("dummy_cached_data")

    if not data:
        time.sleep(2)
        data = "Always generated fresh content (dummy cache)"
        cache.set("dummy_cached_data", data, timeout=60)

    return render(
        request,
        "dummy_cached_page.html",
        {
            "cached": "No (Dummy Cache - No Real Caching)",
            "data": data,
        },
    )
