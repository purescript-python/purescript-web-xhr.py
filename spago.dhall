{-
Welcome to a Spago project!
You can edit this file as you like.
-}
{ name = "purescript-aff"
, dependencies = [ "foreign", "console", "effect", "psci-support" ]
, packages = ./packages.dhall
, sources = [ "src/**/*.purs"]
, backend = "pspy"
}
