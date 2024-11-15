# Import SVG Cuts - Blender Extension

Allows you to import an object from a directory of SVG cuts.

![feature banner](/docs/imgs/featured.png)

## Installation
Install the release [zip file](https://github.com/benedikt-schaber/blender-import-cuts/releases) manually in Blender. See the [Blender Manual](https://docs.blender.org/manual/en/latest/editors/preferences/extensions.html) for more details.

## Usage
The cuts are sorted based on filename in alphabetical order. I thus recommend starting the filename with the number of the cut in the sequence. You should zero pad the number to ensure the cuts are sorted correctly. I.e. use `001`-`999` instead of `1`-`999`.

Once the plugin is installed, you can find the import option in the file menu under `Import -> SVG Cuts Directory (*.svg)`.

### Working with pngs
If your cuts are in the png format you will have to convert them to svg files first. See this [gist](https://gist.github.com/benedikt-schaber/13b6fed6361f390069cd631a23deea5f) for instructions on how to do this.

## Citation
This plugin is open-source and may be freely used in academic research and publications. If you use this plugin in your research, please cite it using github's citation feature in the sidebar or according to the CITATION file.

## For Developers

### Building
```sh
blender --command extension build
```
