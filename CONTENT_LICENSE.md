# CONTENT LICENSE

This file describes the licensing rules for **non-code content** in this repository and related storage.

## Scope

The following types of content are covered by this document:

- Texts: essays, stories, research notes, narratives, in-world documentation.  
- Visuals: images, illustrations, concept art, diagrams, UI mockups, photos of physical works.  
- Audio / video: recorded talks, screencasts, narrative videos, sound design.  
- Identity: logos, characters, world-building elements, visual language, naming schemes explicitly marked as part of the brand identity.

Unless explicitly stated otherwise in a specific file or directory, **all such content is NOT open source**.

## Default rule: All Rights Reserved

By default, all non-code content in directories such as:

- `content/`  
- `portfolio/`  
- `worlds/`  
- any other folders explicitly marked as containing creative or identity material  

is protected by copyright and provided under the following rule:

> © The respective authors. All rights reserved.  
> You may NOT copy, redistribute, modify, or use this content commercially without explicit written permission from the rights holder.

You are allowed to:

- view and explore this content within the system;  
- reference it in discussions and documentation with clear attribution (link to this project and the author, if specified).

You are NOT allowed to:

- republish this content as your own;  
- use it as part of another product, brand, or media project;  
- train proprietary models specifically on this content for commercial purposes without a separate agreement.

## Code vs Content

- **Code** (source files, configuration, scripts) is licensed under the software licenses described in `LICENSE_CORE` and `LICENSE_CLIENTS`.  
- **Content** (as defined above) is governed by this `CONTENT_LICENSE.md` and is not covered by the open source software licenses, unless a specific file explicitly says otherwise.

If you are unsure whether a particular asset is considered code or content, treat it as **content** and assume it is protected.

## Attribution inside the system

Each content unit (note, world, narrative, visual asset) SHOULD, where possible, carry metadata such as:

```yaml
author: <name or handle>
contributors:
  - <handle1>
  - <handle2>
license: "See CONTENT_LICENSE.md"
created_at: YYYY-MM-DD
```

These fields are informational and do not override this license unless an explicit alternative license is specified alongside the asset.

## External platforms (e.g. YouTube, etc.)

When content from this system is published on external platforms (YouTube, social media, blogs), it is:

- subject both to this license and to the terms of the external platform;
- still owned by the original author(s), unless a separate written agreement states otherwise.

If you wish to reuse such content outside the system, please contact the author or project maintainer to negotiate a separate license.
