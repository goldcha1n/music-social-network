window.onload = function() {
    var content = document.getElementById('content');

    for (var i = 0; i < 10; i++) {
        var block = document.createElement('div');
        block.className = 'block';

        var image = document.createElement('img');
        image.alt = 'Изображение';
        image.className = 'block-image';
        block.appendChild(image);

        var artist = document.createElement('h2');
        artist.className = 'block-artist';
        artist.textContent = 'Название исполнителя';
        block.appendChild(artist);

        var track = document.createElement('p');
        track.className = 'block-track';
        track.textContent = 'Название трека';
        block.appendChild(track);

        var audio = document.createElement('audio');
        audio.className = 'block-audio';
        audio.controls = true;
        var source = document.createElement('source');
        source.type = 'audio/mpeg';
        audio.appendChild(source);
        block.appendChild(audio);

        content.appendChild(block);
    }
};
