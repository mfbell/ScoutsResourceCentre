`resources/<type>/<external_id>/<slug>/`
======
Resource detail
------

Detailed view on the resource.

### URL Mapping
- `type`: `activities`, `camps`, `meetings`, `risk-assessments`
- `external_id`: `(?P<external_id>[\w]{6})` E.g. `a1b2c3`
- `slug`: `(?P<slug>[\w-]+)` E.g. `patrol-backwoods-cooking`
