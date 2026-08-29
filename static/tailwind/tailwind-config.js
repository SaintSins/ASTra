tailwind.config = {
    theme: {
      extend: {
        fontFamily: {
          sans: ['Inter', 'sans-serif'],
          serif: ['Playfair Display', 'serif'],
        },
          colors: {
            editorial: {
              bg: '#F9F9F8',      /* Warm, premium off-white */
              text: '#1C1C1C',    /* Deep charcoal */
              muted: '#8A8A8A',   /* Soft grey */
              border: '#EAEAEA'
            }
          },
          typography: (theme) => ({
            editorial: {
              css: {
                '--tw-prose-body': theme('colors.editorial.text'),
                '--tw-prose-headings': theme('colors.editorial.text'),
                '--tw-prose-links': theme('colors.editorial.text'),
                '--tw-prose-hr': theme('colors.editorial.border'),
                fontFamily: theme('fontFamily.sans'),

                img: {
                  borderRadius: '0',                             
                  border: '1px solid',                           
                  borderColor: theme('colors.editorial.border'), 
                  width: '100%',                                 
                  marginTop: '0',                                
                  marginBottom: '2em',                           
                  filter: 'grayscale(100%)',                     
                },
                
                pre: {
                  backgroundColor: theme('colors.editorial.text'),
                  border: '1px solid',
                  borderColor: theme('colors.editorial.border'),
                  color: theme('colors.editorial.bg'),             
                  padding: '1.5rem',
                  borderRadius: '0.375rem',
                  marginTop: '2em',
                  marginBottom: '2em',
                  whiteSpace: 'pre-wrap', 
                  wordBreak: 'break-word',
                },

                'pre code': {
                  backgroundColor: 'transparent',
                  padding: '0',
                  color: 'inherit',
                  fontFamily: theme('fontFamily.sans'),
                  fontSize: '1rem',
                },

                code: {
                  backgroundColor: theme('colors.editorial.border'),
                  color: theme('colors.editorial.text'),
                  padding: '0.2em 0.4em',
                  borderRadius: '0.25rem',
                  fontWeight: '600',
                },

                'code::before': { content: '""' },
                'code::after': { content: '""' },

                blockquote: {
                    borderLeftWidth: '2px',
                    borderColor: theme('colors.editorial.text'),
                    fontStyle: 'normal',
                    fontWeight: '400',
                    paddingLeft: '1.5em',
                  },
                a: {
                      textDecoration: 'none',
                      '&:hover': {
                      color: theme('colors.editorial.muted'),
                      }
                  },
                h1: {
                  fontFamily: theme('fontFamily.serif'),
                  fontWeight: '400',
                  letterSpacing: '-0.02em',
                },
                h2: {
                  fontFamily: theme('fontFamily.sans'),
                  fontWeight: '400',
                },
                h3: {
                  fontFamily: theme('fontFamily.sans'),
                  fontWeight: '500',
                  textTransform: 'uppercase',
                  letterSpacing: '0.05em',
                  fontSize: '1.25rem',
                },
                hr: {
                  borderColor: theme('colors.editorial.border'),
                  borderTopWidth: '1px',
                  marginTop: '3em',
                  marginBottom: '3em',
                },
              },
            },
          }),
        }
      }
    }