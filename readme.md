python ocr

### installation steps

1. compile for [ubuntu](https://code.google.com/p/tesseract-ocr/wiki/Compiling)
2. also download the english training data - I put it in `/usr/local/share/tessdata`
3. ran the [pytesser](https://code.google.com/p/pytesser/) example


### image capture testing

using the free "Lapse It" app for Android


### image processing

crop images to a bounding box:

`convert -crop 318x297+11+14 input.png out.png`

this takes a starting image and crops it to `318 x 297`
starting 11 pixels from the left and 14 pixels from the top.

convert to a higher density greyscale `tif` via:

`convert -density 200 -units PixelsPerInch -type Grayscale +compress input.png output.tif`


### seven-segment training is fun..

1. download digital dream font
2. save a pdf of '0 1 2 3.. :'
3. convert to png via `convert eng.digital-dream.exp0.pdf -density 300 eng.digital-dream.exp0.png`
4. training round one: `tesseract eng.digital-dream.exp0.png eng.digital-dream.exp0 batch.nochop makebox`
5. open image file with moshpytt; make sure letters are boxed correctly; then make correct the identifications
6. feed it back into tesseract: `tesseract eng.digital_dream.exp0.png eng.digital_dream.exp0 nobatch box.train.stderr`
7. generate charset: `unicharset_extractor *.box`
8. create a `font_properties` file with the line `eng.digital_dream.box 0 0 0 0 0`
9. create a shape table: `shapeclustering -F font_properties -U unicharset eng.digital_dream.exp0.tr`
10. mftraining blows up :(

..consider falling back to tesseract 3.0.1

other tutorials talk all about gifs but I think in tess 3.x, png is better
tiffs yielded empty box files and imagemagick conversion was also pretty whack


### other notes
* [ssocr](http://www.unix-ag.uni-kl.de/~auerswal/ssocr/) might be worth testing some more

* a [thread](https://groups.google.com/forum/#!topic/tesseract-ocr/elnIngFJvQs)
on training for seven-segment displays

* these [ocr posts](http://jonathanstreet.com/blog/tag/ocr/)

* more on [training](http://www.sk-spell.sk.cx/first-notes-for-tesseract-ocr-302-traning)
