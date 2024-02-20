# playback-i18n

## Translation files (i18n)

All translation modifications need to be created on a separate branch by running the following commands:

`git checkout -b i18n/update-jp-translation`

You will need to change the name of the branch accordingly. Once your work is done you need to run `git push` and create a PR out of the changes.

### Updating the translation files

In order to translate an `unfinished` entry:

```
<message>
    <location filename="../src/CartDetailsWidget.cpp" line="27"/>
    <source>Unofficial cartridge</source>
    <translation type="unfinished"></translation>
</message>
```

You need to update the `translation` XML property by changing the `unfinished` value to `finished`:

```
<message>
    <location filename="../src/CartDetailsWidget.cpp" line="27" />
    <source>Unofficial cartridge</source>
    <translation type="finished">非公式カートリッジ</translation>
</message>
```

If you're correcting a translation that has the `finished` property, you can simply update the contents inside the `translation` XML tag.

Once you're done updating all entries you need to recompile the translation file and generate a `qm` file by running the command:

`lrelease i18n/main_jp.ts i18n/main_jp.qm`

Now you can recompile the application and the language should be updated.
