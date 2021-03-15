# Next JS

[docs](https://nextjs.org/docs)

## Pages

Pages create routes automatically.

For example, to create `/about`, create `about.js` in `pagees`. [about.js](../next-app/pages/about.js)

### link & router

```javascript
import Link from 'next/link'

<Link href="/about">
    <a className={styles.card}>
        <h3>About &rarr;</h3>
        <p>About page</p>
    </a>
</Link>
```


```javascript
import { useRouter } from 'next/router'

const router = useRouter()

<button onClick={() => router.push('/')}>Home</button>
```


## getInitialProps

A special lifehook in Next. It's a **static, async** function which initializes the props before the page is loaded.