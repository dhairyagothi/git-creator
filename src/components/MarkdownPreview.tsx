import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import rehypeRaw from "rehype-raw";

export function MarkdownPreview({ source }: { source: string }) {
  return (
    <div className="prose-readme">
      <ReactMarkdown
        remarkPlugins={[remarkGfm]}
        rehypePlugins={[rehypeRaw]}
        urlTransform={(value: string) => value}
        components={{
          td: ({ node, ...props }) => {
            const nextProps: Record<string, unknown> = { ...props };
            if ("vAlign" in nextProps) {
              nextProps.valign = nextProps.vAlign as string;
              delete nextProps.vAlign;
            }
            return <td {...nextProps} />;
          },
          th: ({ node, ...props }) => {
            const nextProps: Record<string, unknown> = { ...props };
            if ("vAlign" in nextProps) {
              nextProps.valign = nextProps.vAlign as string;
              delete nextProps.vAlign;
            }
            return <th {...nextProps} />;
          },
          img: ({ node, ...props }) => {
            return (
              <span className="relative inline-block overflow-hidden rounded-md bg-muted/20 align-middle">
                <img 
                  {...props} 
                  loading="lazy"
                  onLoad={(e) => {
                    (e.currentTarget.parentElement as HTMLElement).classList.remove("animate-pulse", "bg-muted/20");
                  }}
                  className="relative z-10 block max-w-full"
                />
                <span className="absolute inset-0 -z-0 animate-shimmer bg-gradient-to-r from-transparent via-white/5 to-transparent bg-[length:200%_100%]" />
              </span>
            );
          },
          ...["div", "p", "h1", "h2", "h3"].reduce((acc, tag) => {
            acc[tag as keyof JSX.IntrinsicElements] = ({ node, ...props }: any) => {
              const nextProps: Record<string, any> = { ...props };
              if ("align" in nextProps) {
                nextProps.style = { ...nextProps.style, textAlign: nextProps.align };
                delete nextProps.align;
              }
              const Tag = tag as any;
              return <Tag {...nextProps} />;
            };
            return acc;
          }, {} as Record<string, React.ElementType>),
        }}
      >
        {source}
      </ReactMarkdown>
    </div>
  );
}
