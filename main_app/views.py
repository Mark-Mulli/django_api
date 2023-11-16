from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from main_app.models import Artist, Song
from main_app.serializers import ArtistSerializer


# Create your views here.
def show(request):
    # artist = Artist.objects.first()
    # print("Artist is ", artist)
    # albums = artist.album_set.all()
    # for alb in albums:
    #     print(alb)
    #     songs = alb.song_set.all()
    #     print("Songs under albums")
    #     for s in songs:
    #         print(s)

    song = Song.objects.first()

    print(song)

    album = song.album

    print(album)

    artists = album.artists.all()

    print(artists)

    for a in artists:
        print(a.name, a.country, a.dob)

    return render(request, 'index.html')


@api_view(['GET', 'POST'])
def api_artists(request):
    if request.method == 'GET':
        artists = Artist.objects.all()
        serializer = ArtistSerializer(instance=artists, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "Artists added", "details": serializer.data})

        return Response({"error": "Invalid Data"})




@api_view(["GET"])
def api_single_artists(request,pk):
    try:
        art = Artist.objects.get(pk=pk)
        serializer = ArtistSerializer(instance=art)
        return Response(serializer.data)
    except:
        return Response({"Error":"Artist by this id does not exist"},status=404)


    return None

@api_view(["DELETE"])

def api_delete_artists(request,pk):
    try:
        art = Artist.objects.get(pk=pk)
        art.delete()
        return Response({"success":"record deleted"})
    except:
        return Response({"Error":"Artist by this id does not exist"},status=404)

    return None

@api_view(["PUT", "PATCH"])
# difference between put and patch
def api_update_artists(request,pk):
    try:
        art = Artist.objects.get(pk=pk)
        serializer = ArtistSerializer(instance=art, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"success":"record updated"})
    except:
        return Response({"Error":"Artist by this id does not exist"},status=404)
    return None