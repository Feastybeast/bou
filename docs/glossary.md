# Glossary

## Bou

The command line tool of `bou`, and project as whole.

## BouDir

The directory containing [Migration](##Migration)s affiliated with a [Database](##Database).

Named as such to connect it conceptually to the [BouFile](##BouFile), which is far more influential.

By default, `bou` suggests `/<directory_of_database>/migrations/`, so `~/myproject/database.sqlite` would have a default *BouDir* of `~/myproject/migrations/`

## BouFile

A metadata file providing basic sanity checking and meta information, stored within the [BouDir](##BouDir).

Assuming our previous settings, it would be `~/myproject/migrations/Boufile.json`

## Database

A sqlite database paired with a [BouFile](##BouFile), which are combined to perform [database migrations](https://en.wikipedia.org/wiki/Schema_migration).

## Migration

A templated python module created by `bou`, which `upgrade()`s or `downgrade()`s a [Database](##Database) based on a given [Route](##Route).

## Route

Calculated during `bou migrate {to_version}`, a *Route*'s direction is determined based on the [Database](##Database)'s current migration version, and the target provided by the user.

`bou` will then incrementally `upgrade()` or `downgrade()` each [Migration](##Migration) step found "along the way".

[Project Homepage](..)