# playback-i18n

## Translation status

| Language            | Type          | Complete | Missing Strings |
| ------------------- | ------------- | -------- | --------------- |
| Simplified Chinese  | Human         | ⚠️        | 15              |
| German              | Human         | ⚠️        | 15              |
| French              | DeepL         | ⚠️       | 79             |
| Spanish             | Human         | ⚠️        | 13              |
| Italian             | DeepL         | ⚠️       | 79             |
| Japanese            | Human         | ⚠️        | 15              |
| Korean              | Human         | ⚠️        | 18             |
| Dutch               | DeepL         | ⚠️       | 74             |

## Translation files (i18n)

All translation modifications need to be created on a separate branch by running the following commands:

`git checkout -b i18n/update-ja-translation`

You will need to change the name of the branch accordingly. Once your work is done you need to run `git push` and create a PR out of the changes.

### Updating translation files with a GUI

Download and install QtLinguist, use it to edit the translation files.

You can download it from [here](https://download.qt.io/linguist_releases/) for Windows. For other OSes you'll need to download Qt6 via a package manager or the online installer Qt provides.

### Updating translation files with a code editor

In order to translate an `unfinished` entry:

```
<message>
    <location filename="../src/CartDetailsWidget.cpp" line="27"/>
    <source>Unofficial cartridge</source>
    <translation type="unfinished"></translation>
</message>
```

You need to update the `translation` XML property by removing the `unfinished` value: 

```
<message>
    <location filename="../src/CartDetailsWidget.cpp" line="27" />
    <source>Unofficial cartridge</source>
    <translation>非公式カートリッジ</translation>
</message>
```

If you're correcting a translation, you can simply update the contents inside the `translation` XML tag.

### Optional compilation

Once you're done updating all entries you need to recompile the translation file and generate a `qm` file by running the command:

`lrelease i18n/main_ja.ts i18n/main_ja.qm`
